from setuptools import setup, find_packages

HYPENATE = '-e .'

def get_requirements(file_path:str)->List[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n",'') for req in requirements]

        if HYPENATE in requirements:
            requirements.remove(HYPENATE)
    return requirements

setup(
    name="scholastic_model_monitor",
    version="0.1",
    author="Vidhya",
    packages=find_packages(),
    #install_requires=["pandas","numpy","seaborn","matplotlib","scikit-learn","xgboost","joblib","flask","flask-restful","flask-cors","gunicorn"]    
    install_requires=get_requirements('requirements.txt')
)