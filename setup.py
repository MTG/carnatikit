from setuptools import find_packages, setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements('requirements.txt')

setup(
    name='carnatikit',
    version="1.0",
    packages=find_packages(),
    author_email=['genis.plaja@upf.edu', 'thomas.nuttall@upf.edu'],
    zip_safe=False,
    include_package_data=True,
    long_description=open('README.md').read(),
    install_requires=install_reqs
)
