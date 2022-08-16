import subprocess
import sys
from setuptools import Extension
from setuptools import setup
import os

def get_long_description():
    with open('README.md') as f:
        long_description = f.read()
    return long_description


#subprocess.run(['pip', "install", "numpy"], check=True)
#subprocess.run(['pip', "install", "cython"], check=True)
#import pip
#pip.main(['install', 'numpy', 'cython']) 

from Cython.Distutils import build_ext
import numpy

os.makedirs('src/octomap/build', exist_ok=True)
subprocess.run(['cmake', ".."], cwd='src/octomap/build', check=True)
subprocess.run(['make'], cwd='src/octomap/build', check=True)

ext_modules = [
    Extension(
        'octomap',
        ['octomap/octomap.pyx'],
        include_dirs=[
            'src/octomap/octomap/include',
            'src/octomap/dynamicEDT3D/include',
            numpy.get_include(),
        ],
        # library_dirs=[
        #     'src/octomap/lib',
        # ],
        # libraries=[
        #     'dynamicedt3d',
        #     'octomap',
        #     'octomath',
        # ],
        language='c++',
        extra_objects=[
            "src/octomap/lib/libdynamicedt3d.a",
            "src/octomap/lib/liboctomap.a",
            "src/octomap/lib/liboctomath.a",
            "src/octomap/lib/liboctovis.a",
        ]
    )
]

setup(
    name='octomap-python',
    version='1.8.0.post12',
    install_requires=['numpy'],
    extras_require={
        'example': ['glooey', 'imgviz', 'pyglet', 'trimesh[easy]'],
    },
    license='BSD',
    maintainer='Kentaro Wada',
    maintainer_email='www.kentaro.wada@gmail.com',
    url='https://github.com/wkentaro/octomap-python',
    description='Python binding of the OctoMap library.',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
)

