# AndroidLocalizationUtil

Simple python script that can help you quickly copy all your language translations in to your android project’s resource files.

## Dependencies

* [lxml](http://lxml.de/) is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.
* [openpyxl](https://openpyxl.readthedocs.io/en/default/) is a Python library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.


## How to use

### Install dependencies

* Install lxml

```
$ pip install lxml
```

* Install openpyxl
```
$ pip install openpyxl
```

### Usage

```
$ python localization.py  [-h] [-v] [-f] excel_file_path|translation_folder_path  project_resource_folder  
```
- -h<br/>
print the usage summary
- -v|--version<br/>
print the version of ther script
- -f|--force(<b>option</b>)<br/>
if the option is provide,the values will be updated if it's already exist,used for update or override translations.
- excel_file_path|translation_folder_path<br/>
the excel file that contains all of the translations to be the input data or the translated resource file
- project_resource_folder<br/>
the android project resource directory

```
Tips: the files in translation_folder_path should like below
folder
  -res
    -values
    -values-ar
    .....

```


## License

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
