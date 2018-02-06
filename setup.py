from distutils.core import setup

setup(
    name='Demopoll',
    version='0.1dev',
    description='Scripts and material to analyze the effect of contextual characteristics on political agreement between local communities in Switzerland',
    url='https://github.com/sjinko/demopoll',
    author='Shin Alexandre Koseki',
    author_email='kosekishin@gmail.com',
    packages=find_packages(),
    license='MIT',
    long_description=open('README.txt').read(),
)
