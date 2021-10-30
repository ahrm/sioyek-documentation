Installation
============

Pre-built Binaries
------------------
You can find the latest pre-built binaries of sioyek here:
https://github.com/ahrm/sioyek/releases

Third-party packages for Linux
------------------------------
If you prefer to install sioyek with a package manager, you can look at this list.
Please note that they are provided by third party packagers.
USE AT YOUR OWN RISK! If you're reporting a bug for a thrid-party package, please mention which package you're using.

+----------+------------------------------------------------------------------------------+------------------------------------------------+
|   Distro |                                Link                                          |                  Maintainer                    |
+==========+==============================================================================+================================================+
|  Arch    |`AUR Sioyek-git <https://aur.archlinux.org/packages/sioyek-git/>`_            | `randomn4me <https://github.com/randomn4me>`_  |
+----------+------------------------------------------------------------------------------+------------------------------------------------+
|  Fedora  |`Copr endle/sioyek <https://copr.fedorainfracloud.org/coprs/endle/sioyek/>`_  | `Endle <https://github.com/Endle>`_            |
+----------+------------------------------------------------------------------------------+------------------------------------------------+


Building from source
--------------------

Linux
^^^^^

1. Install Qt 5 and make sure qmake is in :code:`PATH`.
2. Install :code:`libharfbuzz`:

.. code-block:: console

    $ apt install libharfbuzz-dev

3. Clone the repository and build:

.. code-block:: console

   $ git clone --recursive https://github.com/ahrm/sioyek
   $ cd sioyek
   $ ./build_linux.sh
   
Windows
^^^^^^^

1. Install Visual Studio (tested on 2019, other relatively recent versions should work too)
2. Install Qt 5 and make sure qmake is in :code:`PATH`.
3. Clone the repository and build using 64 bit Visual Studio Developer Commnand Prompt:

.. code-block:: console

   $ git clone --recursive https://github.com/ahrm/sioyek
   $ cd sioyek
   $ build_windows.bat

Mac
^^^

1. Install Xcode and Qt 5.
2. Clone the repository and build:

.. code-block:: console

   $ git clone --recursive https://github.com/ahrm/sioyek
   $ cd sioyek
   $ chmod +x build_mac.sh
   $ ./build_mac.sh
