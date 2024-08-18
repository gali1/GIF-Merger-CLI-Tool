# GIF Merger CLI Tool

A command-line tool for merging multiple GIF files into a single GIF, with options for horizontal or vertical concatenation.

## Getting Started

These instructions will help you set up and run the GIF Merger CLI Tool on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.x and the following libraries installed:

- **Pillow**: Python Imaging Library (PIL) fork
- **tqdm**: Progress bar library

Install these libraries using `pip`:

```bash
pip install pillow tqdm
```

### Installing

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/gif-merger-cli.git
    cd gif-merger-cli
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:

    ```bash
    python gif_merger.py
    ```

### Usage

1. Run the script:

    ```bash
    python gif_merger.py
    ```

2. Follow the prompts:
    - Enter the path to each GIF file you wish to merge.
    - Type `done` when you have finished entering file paths.
    - Specify the output file path (e.g., `output.gif`).
    - Choose the merging orientation (`horizontal` or `vertical`).

3. The merged GIF will be saved to the specified output path.

## Running the Tests

To ensure the script functions as expected, you can run the tests provided. However, this project does not currently include automated tests.

### Manual Testing

1. **Test with sample GIFs**:
    - Create or obtain two or more GIF files.
    - Follow the usage instructions to merge them and verify the output.

2. **Edge Cases**:
    - Test with GIFs of varying dimensions.
    - Check the behavior when fewer than two GIFs are provided.

## Deployment

For deploying this tool, ensure Python and the necessary libraries are installed on the target machine. You may want to package the script and its dependencies into a virtual environment or Docker container for easier deployment.

## Built With

- [Pillow](https://python-pillow.org/) - Python Imaging Library (PIL) fork used for image processing.
- [tqdm](https://tqdm.github.io/) - Progress bar library used for visualizing the process.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/yourusername/gif-merger-cli/tags).

## Authors

* **Your Name** - *Initial work* - [Your GitHub Profile](https://github.com/yourusername)

See also the list of [contributors](https://github.com/yourusername/gif-merger-cli/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Special thanks to contributors and open-source libraries that made this project possible.
* Inspiration drawn from similar tools and community resources.
