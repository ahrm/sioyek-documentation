Scripting and Extensions
========================

Using existing extensions
-------------------------
Before writing your own extensions, you should check out some existing useful extensions in `this repository <https://github.com/ahrm/sioyek-python-extensions>`_, along with instructions on how to enable them in sioyek.

Defining custom commands
------------------------
Sioyek allows you to define your own custom commands and extensions. For example adding this

.. code-block:: console

   new_command _read_selected_text espeak "%{selected_text}"

to your :code:`prefs_user.config` adds a :code:`_read_selected_text` command to sioyek that read the selected text aloud
using espeak (of course you have to have espeak executable in your path). Note that custom command names must begin with an underscore so as not to be confused with built-in sioyek commands.
You can use custom commands the same way you would use sioyek commands. For example you can bind them to keys in your :code:`keys_user.config` like this:


.. code-block:: console

   _read_selected_text <C-r>

or you could search and run them using sioyek's command palette.

.. warning::
   The way we parse :code:`new_command` is very simple: we split the text following the command name by spaces and treat the first part as the name of executable and the rest as parameters. So first of all, you have to escape the spaces in command using backslash. Secondly something like this would not work:

   .. code-block:: console

      new_command _some_command echo "%{file_path}" > somefile.txt
   
   because we would be executing the :code:`echo` command with three parameters: :code:`%{file_path}`, :code:`>` and :code:`somefile.txt`. So if you want to do a complex command using piping, you would have to first create a script that does the piping and call the script from sioyek.

Input parameters
----------------
Sioyek provides the following possible inputs to custom commands:

* :code:`%{file_path}`: expands to current document's full path
* :code:`%{file_name}`: expands to current document's file name
* :code:`%{selected_text}`: expands to current selected text
* :code:`%{selection_begin_document}`: if some text is selected expands to the page number and x and y coordinates in the page's coordinate system of the start of the selection
* :code:`%{selection_end_document}`: if some text is selected expands to the page number and x and y coordinates in the page's coordinate system of the end of the selection
* :code:`%{line_text}`: expands to text of the current selected line when in sioyek's visual line mode
* :code:`%{page_number}`: expands to current page number (zero-indexed)
* :code:`%{command_text}`: If this argument is present in the commands, sioyek prompts the user to enter a text and expands :code:`command_text` to that text.
* :code:`%{mouse_pos_window}`: exapnds to mouse x and y position in window coordinates in pixels
* :code:`%{mouse_pos_document}`: expands to the page number and x and y coordinates of the mouse in the page's coordinate system
* :code:`%{paper_name}`: expands to the paper name under mouse cursor
* :code:`%{sioyek_path}`: expands to the path of sioyek's executable
* :code:`%{local_database}`: expands to the path of sioyek's local database file
* :code:`%{shared_database}`: expands to the path of sioyek's shared database file
* :code:`%{zoom_level}`: expands to the current document's zoom level


.. warning::
   In some builds of sioyek (for example AppImages), :code:`sioyek_path` does not expands to the correct path of the AppImage. In such cases you would have to just manually replace :code:`%{sioyek_path}` with the absolute path of sioyek's executable.


Controlling sioyek
------------------
Scripts can also communicate back to sioyek by executing commands. You can execute all sioyek commands from the command line by running:

.. code-block:: console

   sioyek --execute-command command_name

for example to zoom in, you could run:

.. code-block:: console

   sioyek --execute-command zoom_in

You can also run commands that require text/symbol by specifying :code:`execute-command-data`. For example:

.. code-block:: console

   sioyek --execute-command add_bookmark --execute-command-data "this is a bookmark made from command line"

One of the most useful commands for extensions is :code:`set_status_string` which shows the given text in sioyek's statusbar. For example:

.. code-block:: console

   sioyek --execute-command set_status_string --execute-command-data "this is a status message"

you can clear the status message by running :code:`clear_status_string` command:

.. code-block:: console

   sioyek --execute-command clear_status_string

Of course, instead of running these commands manually, you could automate the process by using any programming language capable of executing command line programs. For example, here is a simple translator in python which shows the translated selected text in sioyek's statusbar:

.. code-block:: python

   import sys
   from googletrans import Translator
   import subprocess

   if __name__ == '__main__':
      sioyek_path = sys.argv[1]
      text = sys.argv[2]
      translator = Translator()
      translation = translator.translate(text, dest='en')
      subprocess.run([sioyek_path, '--execute-command', 'set_status_string', '--execute-command-data', translation.text])

and the corresponding config in :code:`prefs_user.config`:

.. code-block:: console

   new_command _translate python /path/to/translate/script.py "%{sioyek_path}" "%{selected_text}"

We have made a `python wrapper <https://github.com/ahrm/sioyek-python-extensions>`_ around sioyek which makes writing extensions a little easier. You can download it by running:

.. code-block:: console

   pip install sioyek

Using the wrapper, the previous script can be simplified like this:

.. code-block:: python

   import sys
   from googletrans import Translator

   from sioyek import Sioyek, clean_path

   if __name__ == '__main__':
      sioyek_path = clean_path(sys.argv[1])
      text = sys.argv[2]
      sioyek = Sioyek(sioyek_path)
      translator = Translator()
      translation = translator.translate(text, dest='en')
      sioyek.set_status_string(translation.text)

Coordinate spaces
-----------------

All coordinates in database files are in "absolute document space", which might be a little confusing. MuPDF, (the PDF engine that we use) uses something that I call "document space" to specify positions in documents which is the following triplet:

* Page number (zero-indexed)
* x-offset in points relative to the top left of page (1 point = 1/72 inch)
* y-offset in points relative to the top left of page (1 point = 1/72 inch)

In absolute document space, we conceptually view the document as a list of pages stacked vertically. So we don't have page numbers anymore but the y-offset of previous pages are added, so for example, the following page in document space:
:code:`(2, 100, 200)` is translated to the following coordinate in absolute document space: :code:`(100, page_height[0] + page_heights[1] + 200)`.
In order to convert between absolute document space and document space, you can use :code:`to_absolute` and :code:`to_document` functions in https://github.com/ahrm/sioyek-python-extensions/blob/main/src/sioyek/sioyek.py .

Database files
--------------

Sioyek stores all your data in two simple sqlite database files: :code:`local.db` and :code:`shared.db`. Using :code:`%{local_database}` and :code:`%{shared_database}`, you can
pass the file path of these database files to your scripts, which are then allowed to read/write data directly to these files.

.. warning::
   Access to sioyek's local and shared database file is a classic great power/responsibility situation. You could easily wipe out your data if you are not careful. I recommend only adding to database files and deleting only when you know what you are doing.

local database file includes a single table named :code:`document_hash` which maps file paths to their :code:`md5` hash. We later use
this hash to reference files. This allows us to keep bookmarks/highlights even when the document is moved to another location or even another machine.

Shared database files stores all your bookmarks, highlights, etc. The tables in :code:`shared.db` are:

* :code:`bookmarks`: stores the bookmarks. Fields:
   * :code:`document_path`: :code:`md5`-hash of the document (from :code:`document_hash` table in :code:`local.db`)
   * :code:`desc`: the text description of the bookmark
   * :code:`offset_y`: the y-offset of the bookmark in the absolute document space
* :code:`highlights`: stores the highlights. Fields:
   * :code:`document_path`: :code:`md5`-hash of the document
   * :code:`desc`: highlighted text
   * :code:`type`: the type of highlight (the symbol used to create the highlight)
   * :code:`begin_x`: the x-offset of first character of highlight in the absolute document space
   * :code:`begin_y`: the y-offset of first character of highlight in the absolute document space
   * :code:`end_x`: the x-offset of last character of highlight in the absolute document space
   * :code:`end_y`: the y-offset of last character of highlight in the absolute document space
* :code:`links`: stores the portals (they used to be called links but changed their name so as not to be confused with PDF links). Fields:
   * :code:`src_document`: :code:`md5`-hash of the source document
   * :code:`dst_document`: :code:`md5`-hash of the destination document
   * :code:`src_offset_y`: the y-offset of the source document in absolute document space where portal is located
   * :code:`dst_offset_x`: the x-offset of the destination of the portal in absolute document space
   * :code:`dst_offset_y`: the y-offset of the destination of the portal in absolute document space
   * :code:`dst_zoom_level`: the zoom level of the destination of the portal
* :code:`marks`: stores the marks:
   * :code:`document_path`: :code:`md5`-hash of the document
   * :code:`symbol`: The type of the mark (symbol used to create the mark)
   * :code:`offset_y`: The y-offset of the mark in absolute document position
* :code:`opened_books`: stores a list of all opened books along with the current position and zoom level. Fields:
   * :code:`path`: :code:`md5`-hash of the document
   * :code:`offset_x`: current x-offset in the document (in absolute document space)
   * :code:`offset_y`: current x-offset in the document (in absolute document space)
   * :code:`last_access_time`: last time we accessed this document

For an example of how to use database files in extensions, see `this script <https://github.com/ahrm/sioyek-python-extensions/blob/main/src/sioyek/extract_highlights.py>`_ which extracts the highlights of the current document into a new document and creates portals from this new document to the corresponding locations in the original document.
