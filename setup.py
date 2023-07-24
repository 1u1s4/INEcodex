from setuptools import setup, find_packages
setup(
    name='INEcodex',
    version='0.2',
    author='Luis Alfredo Alvarado Rodríguez',
    description='Codificador de datos del INE',
    long_description='',
    url='https://github.com/1u1s4/INEcodex',
    keywords='development, setup, setuptools',
    python_requires='>=3.7',
    packages=find_packages(),
    py_modules=['Codex'],
    install_requires=[
        'pandas',
        'cryptography'
    ],
    package_data={
        'INEcodex': [''],
    },
    include_package_data=True,
)