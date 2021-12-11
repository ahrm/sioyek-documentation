Configuration
=============

Sioyek uses four config files:

- :code:`keys.config` which stores the default keybindings
- :code:`keys_user.config` which stores the modified keybindings
- :code:`prefs.config` which stores the default preferences
- :code:`prefs_user.config` which stores the modified preferences

The location of these files are OS-dependent. You can open these files by executing :code:`keys`, :code:`keys_user`, :code:`prefs` and :code:`prefs_user` commands using the sioyek command line (see :ref:`usage:Command Menu`). 

Syntax of :code:`keys.config` files
-----------------------------------

- Lines starting with :code:`#` are comments and are ignored

.. code-block:: console

   command        k             (command is executed when k is pressed)
   command        <C-k>         (command is executed when k is pressed while holding control)
   command        <S-k>         (command is executed when k is pressed while holding shift)
   command        <A-k>         (command is executed when k is pressed while holding alt)
   command        <S-+>         (command is executed when = is pressed while holding shift.
                                 Note that <S-=> would not work because of a bug in the command system so
                                 when prefixing non-ascii keys with shift, you have to specify the shift
                                 modified key in addition to the shift modifier)
   command        <C-S-k>       (command is executed when k is pressed while holding control and shift)
   command        gg            (command is executed when g is pressed twice)
   command        gt            (command is executed when g is pressed and then t is pressed)
   command        g<C-n><S-d>t  (command is executed when g is pressed and then n is pressed while holding\
                                 control and then d is pressed while holding shift and then t is pressed)


Prefrences in :code:`prefs.config` file
---------------------------------------

:code:`background_color`
^^^^^^^^^^^^^^^^^^^^^^^^
Specifies the background color of the app (this is different from the background color of PDF page, this color is only shown when the displayed page is smaller than the srceen). The syntax to set colors is:

.. code-block:: console

   background_color  r  g  b

where r,g and b red, green and blue values between 0 and 1. For example in order to set the bavkground color to gray we can add the following to our :code:`prefs_user.config`:

.. code-block:: console

   background_color  0.5  0.5  0.5


:code:`dark_mode_background_color`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Specifies the background color when dark mode is enabled.

:code:`dark_mode_contrast`
^^^^^^^^^^^^^^^^^^^^^^^^^^

White text in dark mode can be annoying for the eyes. This option allows us to dim the white colors when dark mode is enabled. Allowed values are between 0.0 and 1.0.

:code:`text_highlight_color`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Highlight color when text is selected using mouse.

:code:`vertical_line_color`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the color of the transparent visual mark explained in :ref:`usage:Underline` (this feature originally had an entirely different functionality which is why it is called vertical line even though there is nothing vertical about it!).
Allowed values are RGBA colors between 0.0 and 1.0. For example, to set the color to a transparent red we add the following to our :code:`prefs_user.config`:

.. code-block:: console

   vertical_line_color  1.0  0.0  0.0  0.1

:code:`search_highlight_color`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The color used to highlight search results.


:code:`link_highlight_color`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The color used to highlight links in PDF files.

:code:`synctex_highlight_color`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Highlight color for synctex forward search highlights.


:code:`search_url_a` to :code:`search_url_z`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The web addresses used for performing :code:`external_search` command. (see :ref:`usage:External Search`). Example:

.. code-block:: console

   search_url_g	https://www.google.com/search?q=

:code:`middle_click_search_engine` and :code:`shift_middle_click_search_engine`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The letter corresponding to :code:`search_url_*` configs to use when middle clicking/shift-middle clicking on text.
Example:

.. code-block:: console

   middle_click_search_engine 		g

This causes the search engine configures using :code:`search_url_g` to be used when middle clicking on text.

:code:`zoom_inc_factor`
^^^^^^^^^^^^^^^^^^^^^^^

The fraction by which we enlarge the page when zooming in/out.


:code:`vertical_move_amount` and :code:`horizontal_move_amount`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

How many inches we move vertically/horizontally when performing move_* commands.

:code:`move_screen_percentage`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The fraction of screen by which we move when executing :code:`screen_down` and :code:`screen_up` commands. (note that despite the name, the values are fractions between 0 and 1, not percentages)

:code:`flat_toc`
^^^^^^^^^^^^^^^^

Displays a simplified flat table of contents instead of a hierarchial one. This can improve performance for documents with very large number of table of contents entries (thousands).
Acceptable values are 0 and 1.

:code:`should_use_multiple_monitors`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If it is 1, when launching the application if we detect multiple monitors, we automatically launch the helper window in second monitor.
Acceptable values are 0 and 1.


:code:`should_load_tutorial_when_no_other_file`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the last opened document is empty, load the tutorial pdf instead.

:code:`should_launch_new_instance`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If it is 0, then we use the previous instance of sioyek when launching a new file, otherwise a new instance is launched every time we open a new file.

:code:`inverse_search_command`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The command to use when trying to do inverse search into a LaTeX document. %1 expands to the name of the file and %2 expans to the line number. For example:

.. code-block:: console

   inverse_search_command 		"C:\path\to\vscode\Code.exe" -r -g %1:%2

:code:`highlight_color_a` to :code:`highlight_color_z`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The color to use for highlights of type :code:`a` to :code:`z`.

:code:`visual_mark_next_page_fraction`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When moving to the next line using visual marker, this setting specifies the distance of the marker to the top of the screen in fractions of screen size when we decite to move the screen.

:code:`visual_mark_next_page_threshold`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When moving to the next line using visual marker, this setting determines at which point we decide to move the screen

:code:`should_draw_unrendered_pages`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If set, we display a checkerboard pattern for unrendered pages (by default we display nothing).

:code:`hover_overview`
^^^^^^^^^^^^^^^^^^^^^^

Displays an overview of destination when hovering over a link with mouse.

:code:`default_dark_mode`
^^^^^^^^^^^^^^^^^^^^^^^^^

Use dark mode by default.

:code:`sort_bookmarks_by_location`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If set, we sort the bookmarks by their location instead of their creation time.

:code:`shared_database_path`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The path of :code:`shared.db` database file. You can set this path to be in a synchronized folder (for example a dropbox folder) and sioyek data will be automatically synchronized across your devices.

:code:`font_size`
^^^^^^^^^^^^^^^^^

Size of the UI font.

:code:`custom_background_color` and :code:`custom_text_color`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Specify the background and text color when using custom color mode (by executing :code:`toggle_custom_color` command).

.. code-block:: console

   custom_background_color		0.18 0.20 0.25
   custom_text_color			1.0 1.0 1.0

:code:`startup_commands`
^^^^^^^^^^^^^^^^^^^^^^^^

Semicolon-separated list of commands to execute on startup. For example, to start in custom color mode and in visual scroll mode, you can add the following (the command names are the same as the ones displayed when opening the command window using :code:`:`):

.. code-block:: console

   startup_commands		toggle_custom_color;toggle_visual_scroll