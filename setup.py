from setuptools import setup, find_packages

setup(
    name='fish',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here
        
    ],
    entry_points={
        'console_scripts': [
            'fish_app=app:main',  # Replace 'app' and 'main' with your actual module and function
        ],
    },
)
