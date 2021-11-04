from setuptools import setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='uleska-automate',
    version='0.5.0',
    description='Command line tool to run scans on Uleska',
    py_modules=['uleskaautomate'],
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/uleska/uleska-automate',
    author='Gary Robinson',
    author_email='gary.robinson@uleska.com',
    install_requires = ['requests ~= 2.26'],
    extras_require = {
        'dev': ['pytest>=3.7', 'mockito'],
    }, 
)