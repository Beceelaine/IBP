from setuptools import setup

setup(
      name='IBP',
      version=1.0,
      url='https://github.com/Beceelaine/Indian-Buffet-Process',
      description='Infinite Latent Feature Models and the Indian Buffet Process',
      author='Wenwen Ye, Kuazhuo Zhang',
      license='BSD',
      packages=['IBP'],,
      include_package_data=True,
      zip_safe=False,
      entry_points={
      'console_scripts': ['scrapy = scrapy.cmdline:execute']
      },
      install_requires=[],
      )
