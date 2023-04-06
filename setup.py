from setuptools import setup


setup(
    name='crowdnav',
    version='0.0.1',
    packages=[
        'crowd_nav',
        'crowd_nav.configs',
        'crowd_nav.policy',
        'crowd_nav.utils',
        'crowd_sim',
        'crowd_sim.envs',
        'crowd_sim.envs.policy',
        'crowd_sim.envs.utils',
    ],
    install_requires=[
        'gitpython',
        'gym==0.13.0',
        'matplotlib',
        'numpy',
        'scipy',
        'torch==1.4.0',
        'torchvision==0.5.0',
        'seaborn',
        'tqdm',
        'tensorboardX'
    ],
    extras_require={
        'test': [
            'pylint',
            'pytest',
        ],
    },
)
