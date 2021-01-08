from distutils.core import setup
setup(
    name = 'glitch_effects',
    packages = ['glitch_effects'],
    version = '0.0.1',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Apply glitch effects to images, and create animated versions.',
    author = 'Ethan Swartzentruber',
    author_email = 'eswartzen@gmail.com',
    url = 'https://github.com/epswartz/glitch_effects',
    download_url='https://github.com/epswartz/glitch_effects/archive/0.0.2.zip',
    keywords = ['glitch', 'effects', 'image', 'image processing', 'vfx'],
    install_requires=[            # I get to this in a second
        'Pillow',
        'numpy',
        'rich',
        'scikit-image',
        'typer'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: End Users/Desktop',
        'Topic :: Artistic Software',
        #'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.8'
    ],
)
