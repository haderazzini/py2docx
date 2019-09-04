'''
###############################################################################
#                Create a docx from all .py files in directory                #
###############################################################################
#   version     date        author              comments                      #
###############################################################################
#   0.0.1       2019-09-04  Hader Azzini         innitial                     #
###############################################################################
'''

import os

from entities.check_directory import ReaderDirectory


if __name__ == "__main__":

    rd = ReaderDirectory()

    target_directory = r'folder_example'

    full_path_directory = os.path.abspath(target_directory)

    docx_name = 'documentation' #save in target directory
    title_inside_docx = 'Plataforma para Desenvolvimento e Teste de Abordagens de Desagregação de Cargas Elétricas Residenciais.'

    rd.py2pdf(full_path_directory,title=title_inside_docx,docx_name=docx_name)