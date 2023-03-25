from PyQt5 import QtWidgets, QtGui, QtCore

from moviepy.editor import concatenate_videoclips, ImageClip

import os
import sys
from typing import List

from ui_mainwindow import Ui_MainWindow
from ui_progress import Ui_Dialog as UI_ProgressWindow


class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    failed = QtCore.pyqtSignal()

    def __init__(self, images: List[str], output: str, duration: int, parent=None):
        super().__init__(parent)
        self.images = images
        self.output = output
        self.duration = duration

    def run(self) -> None:
        try:
            clips = []
            for i in self.images:
                clips.append(ImageClip(i, duration=self.duration))
            concatenated = concatenate_videoclips(clips, method="compose")
            concatenated.write_videofile(self.output, fps=24)
            self.finished.emit()
        except Exception as e:
            print(e)
            self.failed.emit()


class ProgressWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UI_ProgressWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.progress_win = None
        self.thread = None
        self.worker = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.workdir = os.getenv("HOME", ".")

        self.ui.lstImages.itemSelectionChanged.connect(self.images_selection_changed)
        self.ui.btnLoadImage.clicked.connect(self.btn_load_image_clicked)
        self.ui.btnLoadFolder.clicked.connect(self.btn_load_folder_clicked)
        self.ui.btnBrowseOutput.clicked.connect(self.btn_browse_output_clicked)
        self.ui.btnNextImage.clicked.connect(self.btn_next_image_clicked)
        self.ui.btnRemoveImage.clicked.connect(self.btn_remove_image_clicked)
        self.ui.btnPreviousImage.clicked.connect(self.btn_previous_image_clicked)
        self.ui.dialImageDuration.valueChanged.connect(self.sld_image_duration_changed)
        self.ui.btnRender.clicked.connect(self.btn_render_clicked)

    def render_finished(self):
        QtWidgets.QMessageBox.information(self.progress_win, "Rendern beendet", "Rendern erfolgreich!")

    def render_failed(self):
        QtWidgets.QMessageBox.critical(self.progress_win, "Rendern beendet", "Rendern fehlgeschlagen!")

    def btn_render_clicked(self):
        self.thread = QtCore.QThread()
        self.progress_win = ProgressWindow()
        images = []
        for i in range(self.ui.lstImages.count()):
            images.append(self.ui.lstImages.item(i).text())
        print(images)
        self.worker = Worker(images, self.ui.edtOutputPath.text(), self.ui.dialImageDuration.value())
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.failed.connect(self.thread.quit)
        self.worker.failed.connect(self.worker.deleteLater)

        self.worker.failed.connect(self.render_failed)
        self.worker.finished.connect(self.render_finished)

        self.worker.failed.connect(self.progress_win.close)
        self.worker.finished.connect(self.progress_win.close)

        self.thread.start()
        self.progress_win.exec()

    def sld_image_duration_changed(self):
        self.ui.lblImageDuration.setText(f"Dauer pro Folie: {self.ui.dialImageDuration.value()}s")

    def btn_remove_image_clicked(self):
        for i in self.ui.lstImages.selectedItems():
            self.ui.lstImages.takeItem(self.ui.lstImages.row(i))

    def btn_next_image_clicked(self):
        if self.ui.lstImages.currentRow() == self.ui.lstImages.count() - 1:
            self.ui.lstImages.setCurrentRow(0)
        else:
            self.ui.lstImages.setCurrentRow(self.ui.lstImages.currentRow() + 1)

    def btn_previous_image_clicked(self):
        if self.ui.lstImages.currentRow() == 0:
            self.ui.lstImages.setCurrentRow(self.ui.lstImages.count() - 1)
        else:
            self.ui.lstImages.setCurrentRow(self.ui.lstImages.currentRow() - 1)

    def btn_browse_output_clicked(self):
        video_location = QtWidgets.QFileDialog.getSaveFileName(self,
                                                               "Speichern unter", self.workdir, "Video (*.mp4")[0]
        if not video_location:
            return
        if os.path.splitext(video_location)[1] != ".mp4":
            video_location += ".mp4"
        self.ui.edtOutputPath.setText(video_location)
        self.workdir = os.path.dirname(video_location)

    def btn_load_folder_clicked(self):
        new_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Ordner öffnen...", self.workdir)
        files = []
        if new_dir == "":
            return
        for i in os.listdir(new_dir):
            if os.path.splitext(i)[1] in [".png", ".jpg"]:
                files.append(os.path.join(new_dir, i))
        self.ui.lstImages.addItems(files)
        self.workdir = new_dir
        self.ui.edtOutputPath.setText(os.path.join(new_dir, "Vorspann.mp4"))

    def images_selection_changed(self):
        if len(self.ui.lstImages.selectedItems()) == 0:
            self.ui.btnRemoveImage.setEnabled(False)
            self.ui.btnPreviousImage.setEnabled(False)
            self.ui.btnNextImage.setEnabled(False)
            self.ui.preview.setText("Kein Bild geladen.")
            return

        self.ui.btnRemoveImage.setEnabled(True)
        self.ui.btnPreviousImage.setEnabled(True)
        self.ui.btnNextImage.setEnabled(True)
        self.ui.preview.setPixmap(QtGui.QPixmap(self.ui.lstImages.currentItem().text()).
                                  scaled(self.ui.preview.width(), self.ui.preview.height(),
                                         QtCore.Qt.KeepAspectRatio))

    def btn_load_image_clicked(self):
        filepath = QtWidgets.QFileDialog.getOpenFileNames(self, "Bilder laden...", self.workdir,
                                                          "Bilder (*.png *.jpg)")

        self.ui.lstImages.addItems(filepath[0])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())
