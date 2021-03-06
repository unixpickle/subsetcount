from setuptools import setup

setup(
    name='subsetcount',
    version='0.0.1',
    description='Measure the probability that a sentence only uses some characters.',
    url='https://github.com/unixpickle/subsetcount',
    author='Alex Nichol',
    author_email='unixpickle@gmail.com',
    license='BSD',
    install_requires=[
        'numpy>=1.0.0,<2.0.0',
        'anyrl>=0.12.13,<0.13.0',
        'xformer>=1.0.1,<2.0.0',
    ],
    extras_require={
        "tf": ["tensorflow>=1.0.0"],
        "tf_gpu": ["tensorflow-gpu>=1.0.0"],
    },
)
