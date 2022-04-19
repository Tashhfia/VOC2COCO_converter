# PASCAL VOC TO COCO SCRIPT
## Usage steps:

1. Generate paths to xml files using the generate_anno_path script. Update the code before running it!
2. Modify labels.txt and add your class/label names. One class name per line
3. Run voc2coco:  python voc2coco.py --ann_paths_list /path/to/annotation/paths.txt --labels /path/to/labels.txt --output /path/to/output.json

	Eg-

		python voc2coco.py --ann_paths_list paths.txt --labels labels.txt --output trainOutput.json

4. Add the following info to the json file. Edit as needed...
{info": {"description": null, "url": null, "version": null, "year": 2022, "contributor": null, "date_created": "2022-04-19 11:31:08.350302"}, "licenses": [{"url": null, "id": 0, "name": null}],
