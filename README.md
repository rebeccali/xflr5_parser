This script is used to parse XFLR5 files into CSV files. Run it using:

`python3 xflr5_polar_parser -i myfolder -o myfile.csv`

`myfolder` should be a folder full of polars with different flap deflections.
The foil should be named "somefoil blah balh d10" where 10 would be the flap deflection amount.

## Workflow
The workflow for generating a new set of deflected foils looks like:
1. Go into XFLR5 and generate a bunch of foils labeled "foil d0", "foil d5"..
2. Export polars using Polars > Export All Polars > New folder
3. Run `python3 xflr5_polar_parser -i myfolder -o myfile.csv`


## Tests:

A whole folder:
`python3 xflr5_polar_parser.py -f raw_polars/ -o allPolars.csv`

A single file:
`python3 xflr5_polar_parser.py -i testPolar.txt -o testPolar.csv`


## Requirements:
* pandas
* argparse
