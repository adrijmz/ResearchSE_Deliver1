import os
import unittest
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.script import generate_keyword_cloud
from src.script import clear_links_file


class TestFiles(unittest.TestCase):
    def is_pdf_file(self):
        _, file_extension = os.path.splitext(self.file_path)
        return file_extension.lower() == '.pdf'

    # Test to check if all files in the papers folder are PDF
    def test_all_files_are_pdf(self):
        folder_path = './papers'
        files = os.listdir(folder_path)
        for file in files:
            self.file_path = os.path.join(folder_path, file)
            self.assertTrue(self.is_pdf_file())

    # Test to check if the links file is empty
    def test_is_empty_document(self):
        clear_links_file('./output')
        with open('./output/links.txt', 'r') as f:
            self.assertEqual(f.read(), '')


class TestKeywordCloudGeneration(unittest.TestCase):

    # Test to check if the keyword cloud is generated
    def test_keyword_cloud_generation(self):
        abstract = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
                    "labore et dolore magna aliqua. Nisl purus in mollis nunc sed id semper risus in. Ac odio tempor "
                    "orci dapibus ultrices in iaculis. Egestas sed sed risus pretium quam vulputate dignissim. Orci "
                    "porta non pulvinar neque laoreet suspendisse. Pharetra massa massa ultricies mi quis. "
                    "Suspendisse faucibus interdum posuere lorem. Amet nisl purus in mollis nunc sed. Morbi tempus "
                    "iaculis urna id volutpat lacus laoreet non curabitur. Felis imperdiet proin fermentum leo vel "
                    "orci porta non. Nisl tincidunt eget nullam non nisi est sit amet facilisis. Quis auctor elit sed "
                    "vulputate. Sed libero enim sed faucibus turpis. A condimentum vitae sapien pellentesque. Sem "
                    "viverra aliquet eget sit amet. Mauris sit amet massa vitae tortor.")

        generate_keyword_cloud(abstract, './output')
        self.assertTrue(os.path.exists('./output/keyword_cloud.png'))


if __name__ == '__main__':
    unittest.main()
