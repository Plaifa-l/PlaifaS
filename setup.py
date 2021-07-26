from distutils.core import setup

try:
  with open("README.md","r") as fh:
    long_description = fh.read()
except:
  long_description = 'OOP learning example by Plaifa Laokittichai'

setup(
  name = 'PlaifaS',         # How you named your package folder (MyLib)
  packages = ['PlaifaS'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'OOP learning example by Plaifa Laokittichai',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type = "text/markdown",
  author = 'Loong Wissawakorn',                   # Type in your name
  author_email = 'r.innovative1@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Plaifa-l/PlaifaS',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Plaifa-l/PlaifaS/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['OOP', 'Thai', 'Plai'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)