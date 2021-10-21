@echo off & color 8F

echo                              ___-----------___
echo                        __--~~                 ~~--__
echo                    _-~~                             ~~-_
echo                 _-~                                     ~-_
echo                /                                           \
echo               ^|                                             ^|
echo              ^|                                               ^|
echo              ^|                                               ^|
echo             ^|                                                 ^|
echo             ^|                                                 ^|
echo             ^|                                                 ^|
echo              ^|                                               ^|
echo              ^|  ^|    _-------_               _-------_    ^|  ^|
echo              ^|  ^|  /~         ~\           /~         ~\  ^|  ^|
echo               ^|^|  ^|             ^|         ^|             ^|  ^|^|
echo               ^|^| ^|               ^|       ^|               ^| ^|^|
echo               ^|^| ^|              ^|         ^|              ^| ^|^|
echo               ^|   \_           /           \           _/   ^|
echo              ^|      ~~--_____-~    /~V~\    ~-_____--~~      ^|
echo              ^|                    ^|     ^|                    ^|
echo             ^|                    ^|       ^|                    ^|
echo             ^|                    ^|  /^\  ^|                    ^|
echo              ^|                    ~~   ~~                    ^|
echo               \_         _                       _         _/
echo                 ~--____-~ ~\                   /~ ~-____--~
echo                      \     /\                 /\     /
echo                       \    ^| ( ,           , ) ^|    /
echo                        ^|   ^| (~(__(  ^|  )__)~) ^|   ^|
echo                         ^|   \/ (  (~~^|~~)  ) \/   ^|
echo                          ^|   ^|  [ [  ^|  ] ]  /   ^|
echo                           ^|                     ^|         
echo                            \                   /
echo                             ~-_             _-~
echo                                ~--___-___--~

cd "%~dp0\src"
pip uninstall discord.py
pip uninstall discord
pip install -r requirements.txt