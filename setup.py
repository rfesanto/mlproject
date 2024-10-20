from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() ## le as linhas do arquivo de entrada
        requirements=[req.replace("\n","") for req in requirements] # a cada linha ele gera uma letra "n". substitui por campo em branco

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) ## no arquivo requirements tem o '-e .' que faz com que ele seja linkado ao setup. remove esse termpo para não tentar instalar como pacote
    
    return requirements

setup(
    
name='mlproject',
version='0.0.1',
author='rsanto',
author_email='rafael.faria3@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)