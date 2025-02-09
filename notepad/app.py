from PyQt6.QtCore import QFileInfo
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QPinchGesture
import sys
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from notepad import Ui_MainWindow



class NotePadWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.actionSave.triggered.connect(self.save_file)
        self.actionNew.triggered.connect(self.file_new)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionPrint_Preview.triggered.connect(self.preview_dialog)
        self.actionExport_PDF.triggered.connect(self.export_pdf)


    def maybe_save(self):
        if not self.textEdit.document().isModified():
            return True

        ret = QMessageBox.warning(self, "Application", "The Document han been modified. \n Do you want to save your changes ? "
                                  , QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Save:
            return self.save_file()

        if ret == QMessageBox.StandardButton.Cancel:
            return False

        return True

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')

        if(filename[0]):
            f = open(filename[0], 'w')

            with f:
                text = self.textEdit.toPlainText()
                f.write(text)
                QMessageBox.about(self, 'Save File', 'File Has Been saved')


    def file_new(self):
        if self.maybe_save():
            self.textEdit.clear()

    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printer)

    def preview_dialog(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec()


    def print_preview(self, printer):
        self.textEdit.print(printer)


    def export_pdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', "PDF files (.pdf) ;; All Files()")

        if fn != "":
            if QFileInfo(fn).suffix() == "" : fn += '.pdf'
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print(printer)


app = QApplication(sys.argv)
Note = NotePadWindow()
sys.exit(app.exec())