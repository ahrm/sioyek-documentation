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
Specifies the background color of the app (this is different from the background color of PDF page which is configured using :ref:`customcolor`, this color is only shown when the displayed page is smaller than the srceen). The syntax to set colors is:

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

:code:`visual_mark_color`
^^^^^^^^^^^^^^^^^^^^^^^^^

This is the color of the transparent visual mark explained in :ref:`usage:Visual Mark` (this feature originally had an entirely different functionality which is why it is called vertical line even though there is nothing vertical about it!).
Allowed values are RGBA colors between 0.0 and 1.0. For example, to set the color to a transparent red we add the following to our :code:`prefs_user.config`:

.. code-block:: console

   visual_mark_color  1.0  0.0  0.0  0.1

:code:`ruler_mode`
^^^^^^^^^^^^^^^^^^

If it is 1, we highlight a rectangle around the current line in visual mark mode. Otherwise, we highlight below the current line.

.. code-block:: console

   ruler_mode  1

:code:`ruler_padding` and :code:`ruler_x_padding`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Additional padding for ruler. Makes the ruler a little larger and more readable.

.. code-block:: console

   ruler_padding 1.0
   ruler_x_padding 5.0

:code:`visual_mark_next_page_fraction`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When we go to the next page while in visual mark mode, this setting determines which location of screen the new line should be located at. The values are between -1 and 1. With 0 being the middle of the screen and 1 and -1 being the top and bottom of the screen respectively.

.. code-block:: console

   visual_mark_next_page_fraction  0.5

:code:`visual_mark_next_page_threshold`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Determines at which point in screen we move to the next page. Acceptable range is between 0 and :code:`visual_mark_next_page_fraction`.

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

:code:`wheel_zoom_on_cursor`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If set, when using mouse wheel to zoom we zoom in on mouse cursor instead of middle of screen.


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

:code:`collapsed_toc`
^^^^^^^^^^^^^^^^^^^^^

If set, we initially collapse all table of content entries.

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

:code:`should_draw_unrendered_pages`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If set, we display a checkerboard pattern for unrendered pages (by default we display nothing).

:code:`hover_overview`
^^^^^^^^^^^^^^^^^^^^^^

Displays an overview of destination when hovering over a link with mouse.

:code:`rerender_overview`
^^^^^^^^^^^^^^^^^^^^^^^^^

Normally we reuse the rendered page for overview window. This may cause the overview page to be blurry or too sharp if there is a significant difference between the zoom levels of the main window and overview window.
If :code:`rerender_overview` is set, we rerender overview which solves this issue at the cost of some additional computation.

.. code-block:: console

   rerender_overview		1

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

:code:`ui_font`
^^^^^^^^^^^^^^^^^^^^^^^^

The font to use for UI text.

.. code-block:: console

   ui_font		Segoe UI Emoji


:code:`item_list_prefix`
^^^^^^^^^^^^^^^^^^^^^^^^

A prefix character to use before list of items (for example can be used to display a checkmark before each of the bookmarks).

.. code-block:: console

   item_list_prefix	✔️

:code:`check_for_updates_on_startup`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If set, sioyek checkes for new versions on startup and notifies the user if a new version if available.

.. code-block:: console

   check_for_updates_on_startup	1

.. _customcolor:

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

:code:`status_bar_color`, :code:`status_bar_text_color` and :code:`status_bar_font_size`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Allow you to customize the appearance of status bar.

.. code-block:: console

   status_bar_color        0 0 0
   status_bar_text_color   1 1 1
   status_bar_font_size    10

:code:`execute_command_a` to :code:`execute_command_z`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Predefined shell commands to be executed using :code:`execute_predefined_command`. :code:`%1` expands to the path of the current file, :code:`%2` expands to name of the current file and :code:`%3` expands to current selected text.
For example, suppose you have a command named :code:`ocr` which takes a file path and produces an OCR'd version of the document. You can add the following to you :code:`prefs_user.config`:

.. code-block:: console

   execute_command_o	ocr "%1"

You can later quickly invoke this command by executing :code:`execute_predefined_command` and then pressing :code:`o`.

.. warning::
   The command parsing code in sioyek is not very good. For example it can not handle multiple commands like :code:`command1 args;command2` or commands that include spaces. If you want to run a complex command, first put all commands in a script file and then run the script file using using sioyek like this: :code:`/path/to/script.sh %1 %2 %3`.

:code:`papers_folder_path`
^^^^^^^^^^^^^^^^^^^^^^^^^^

Path to a directory on your computer. Sioyek monitors the changes in this directory and if a new file is added to this directory while we have a pending portal, this file is automatically used as the destination of the portal. This is useful when creating a portal from a reference in a paper to the actual reference file.

:code:`display_resolution_scale`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Manual resolution scaling. Can be useful for some very high resolution displays which report the wrong resolution.

:code:`linear_filter`
^^^^^^^^^^^^^^^^^^^^^^

If set, we use linear texture filtering instead of the normal nearest neighbour filtering. This is useful when using manual display resolution scale which causes the nearest neighbour filter to look bad.

:code:`main_window_size`, :code:`main_window_move`, :code:`helper_window_size`, :code:`helper_window_move`, :code:`single_main_window_size` and :code:`single_main_window_move`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configures the size and position of the main window and the helper window. :code:`single_main_window_*` is used when helper window is closed and the other configs are used when both windows are opened. 
These values are automatically written to :code:`auto.cong` file when sioyek exits but you can manually override them by setting them in your :code:`prefs_user.config`.

.. code-block:: console

   single_main_window_size    1824 988
   single_main_window_move     22 21
   main_window_size    1824 988
   main_window_move     18 44
   helper_window_size    1891 1033
   helper_window_move     1951 0

:code:`touchpad_sensitivity`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Can be used to adjust the sensitivity of the touchpad. 

.. code-block:: console

   touchpad_sensitivity    0.1

:code:`page_separator_width` and :code:`page_separator_color`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to adjust the appearance of page separator.

.. code-block:: console

   page_separator_width 2
   page_separator_color 0.5 0.5 0.5

:code:`fit_to_page_width_ratio`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ratio of screen width to use when using :code:`fit_to_screen_width_ratio` command. Can be useful for very wide screens.

.. code-block:: console

   fit_to_page_width_ratio 0.75

:code:`create_table_of_contents_if_not_exists`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If set and the file doesn't have a table of contents, we use heuristic methods to create a table of contents. You can use :code:`max_created_toc_size` to prevent creating very large table of contents.

.. code-block:: console

   create_table_of_contents_if_not_exists 1
   max_created_toc_size 5000

:code:`force_custom_line_algorithm`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use legacy line detection algorithm instead of the mupdf one.

:code:`overview_size` and :code:`overview_offset`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adjust the size of overview window. The values are in normalized window coordinates between -1 and 1.

.. code-block:: console

   overview_size 0.852604 0.597729
   overview_offset -0.0119792 0.120151