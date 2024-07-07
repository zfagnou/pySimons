from setuptools import setup, find_packages

setup(
    name='PyQuant',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy', 'pandas'
    ],
    entry_points={
        'console_scripts': [
            # Add command line scripts if needed
        ],
    },
    author='Zachary Fagnou',
    author_email='zfagnou3@gmail.com',
    description='A package for generating synthetic corporate finance data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/finance_tools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
