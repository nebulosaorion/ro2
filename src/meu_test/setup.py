from setuptools import setup

package_name = 'meu_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=['meu_test'], 
    install_requires=['setuptools', 'rclpy', 'geometry_msgs'],
    zip_safe=True,
    author='Seu Nome',
    author_email='seu-email@dominio.com',
    description='Descrição do seu pacote',
    long_description='Descrição longa do seu pacote',
    long_description_content_type='text/markdown',
    keywords=['ROS 2', 'meu_test'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'move_listener = meu_test.move_listener:main',
        ],
    },
)

