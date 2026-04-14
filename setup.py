from setuptools import setup, find_packages
with open('requirements.txt','r') as f:
    requirements = f.read().splitlines()
setup(
    name='mlopsProject',
    version='0.0.1',
    Repo_name = 'Mlops-end',
    author='kamlesh',
    author_email='kamlesh.jambani@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
)