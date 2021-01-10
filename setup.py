from distutils.core import setup


VERSION="0.1.0"

setup(
    name = 'glitch_effects',
    version = VERSION,
    packages = ['glitch_effects'],
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Apply glitch effects to images, and create animated versions.',
    author = 'Ethan Swartzentruber',
    author_email = 'eswartzen@gmail.com',
    url = 'https://github.com/epswartz/glitch_effects',
    download_url=f'https://github.com/epswartz/glitch_effects/archive/{VERSION}.zip',
    keywords = ['glitch', 'effects', 'image', 'image processing', 'vfx'],
    install_requires=[            # I get to this in a second
        'Pillow',
        'numpy',
        'rich',
        'scikit-image',
        'typer'
    ],
    classifiers=[
        'Development Status :: 4 - Beta', # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: End Users/Desktop',
        'Topic :: Artistic Software',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': ['glitch=glitch_effects.cli:main']
    }
)
