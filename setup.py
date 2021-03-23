from setuptools import setup, find_packages

setup(
    name='rscphil',
    packages=find_packages(),
    version='0.0.1',
    license='MIT',
    author='Waqas Nazir',
    author_email='waqasnazir03@gmail.com',
    url='https://github.com/waqasnazir03/rscphil',
    keywords=['openstack', 'cloud'],
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        rscphil=rscphil.cli.main:main
    '''
)
    
