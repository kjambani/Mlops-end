from setuptools import setup, find_packages
with open('requirements.txt','r') as f:
    requirements = [req.strip() for req in f.read().splitlines() if req.strip() and not req.startswith('-e')]
setup(
    name='mlopsProject',
    version='0.0.1',
    author='kamlesh',
    author_email='kamlesh.jambani@gmail.com',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements,
)