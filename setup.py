import setuptools

version = '0.0.1'

setuptools.setup(
    name='tree_stat',
    version=version,
    author='Adrien Horgnies',
    author_email='adrien.pierre.horgnies@gmail.com',
    description='CLI script to measure the volume of a directory tree',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['pyyaml', 'mysql_tracer', 'Jinja2'],
    entry_points={
        'console_scripts': ['tree_stat=tree_stat.__main__:main']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Alpha'
    ],
    keywords=[]
)