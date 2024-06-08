| Command                           | Description                                            |
| --------------------------------- | ------------------------------------------------------ |
| `poetry new [package-name]`       | Start a new Python Project.                            |
| `poetry init`                     | Create a _pyproject.toml_ file interactively.          |
| `poetry install`                  | Install the packages inside the _pyproject.toml_ file. |
| `poetry add [package-name]`       | Add a package to a Virtual Environment.                |
| `poetry add -D [package-name]`    | Add a dev package to a Virtual Environment.            |
| `poetry remove [package-name]`    | Remove a package from a Virtual Environment.           |
| `poetry remove -D [package-name]` | Remove a dev package from a Virtual Environment.       |
| `poetry self:update`              | Update poetry to the latest stable version.            |

In a <router-link to="/blog/python-projects-with-poetry-and-vscode-part-2">second article</router-link>, we will see more _Poetry_ commands, add our Virtual Environment to _VSCode_ and use the dev packages we installed to lint (Flake8), format (Black) and test (Pytest) our code inside the editor. Finally, in a third one, we will write and publish a sample library to _PyPI_.
