import os
import unittest

def is_pdf_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.pdf'

class TestFileFormat(unittest.TestCase):
    def test_all_files_are_pdf(self):
        folder_path = 'papers'
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            self.assertTrue(is_pdf_file(file_path))

if __name__ == '__main__':
    unittest.main()