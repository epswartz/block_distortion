from distutils.core import setup


VERSION="0.0.1"

setup(
    name = 'block_distortion',
    version = VERSION,
    packages = ['block_distortion'],
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Apply block distortion effects to images, and create animated versions.',
    author = 'Ethan Swartzentruber',
    author_email = 'eswartzen@gmail.com',
    url = 'https://github.com/epswartz/block_distortion',
    download_url=f'https://github.com/epswartz/block_distortion/archive/{VERSION}.zip',
    keywords = ['distortion', 'glitch', 'effects', 'image', 'image processing', 'vfx'],
    install_requires=[            # I get to this in a second
        'Pillow',
        'numpy',
        'rich',
        'scikit-image',
        'typer'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable', # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: End Users/Desktop',
        'Topic :: Artistic Software',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': ['block_dist=block_distortion.cli:main']
    }
)
