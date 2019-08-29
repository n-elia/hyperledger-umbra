from setuptools import setup, find_packages

setup(name='umbra-orch',
      version='0.1',
      description='Hyperledger Labs: Project Umbra - Orchestration System',
      author='Raphael Vicente Rosa',
      packages=find_packages(),
      include_package_data=True,
      platforms='any',
      keywords=('Hyperledger', 'Labs', 'Umbra'),
      license='Apache License v2.0',
      url='https://github.com/raphaelvrosa/umbra',
      download_url='https://github.com/raphaelvrosa/umbra',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
      ],
      install_requires = [
        'asyncio',
        'aiohttp',
        'colorlog',
      ],
)
