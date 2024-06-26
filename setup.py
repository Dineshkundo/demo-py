from setuptools import setup, find_packages

setup(
    name='fish',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'click==8.1.3',
        'colorama==0.4.5',
        'Flask==2.2.2',
        'importlib-metadata==4.12.0',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.2',
        'joblib==1.1.0',
        'MarkupSafe==2.1.1',
        'numpy',
        'pandas',
        'python-dateutil==2.8.2',
        'pytz==2022.2.1',
        'scipy',
        'six==1.16.0',
        'scikit-learn',
        'threadpoolctl==3.1.0',
        'Werkzeug==2.2.2',
        'zipp==3.8.1',
        'gunicorn==20.0.4'
    ],
    entry_points={
        'console_scripts': [
            'fish_app=app:main',  # Adjust this based on your app's entry point
        ],
    },
)
