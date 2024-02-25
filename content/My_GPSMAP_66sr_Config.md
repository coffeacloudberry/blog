Title: My GPSMAP 66sr Config
Date: 2024-02-25 00:00
Category: Outdoor Tips
Summary: My handheld GPS configuration for hiking

I have the Garmin GPSMAP 64sc and recently upgraded to the GPSMAP 66sr for a better screen and GPS signal. This article is not a device review but how I set it up to my needs as a hiker and backcountry skier. Basically, map quality, battery, and fast startup are important. The [multi-band GPS](https://support.garmin.com/en-US/?faq=jptru9E32f6q0zydcdtXh9) chip in the 66sr has a faster time to fix (time to locate after startup) and better signal stability than the 64sc.

![Multi-band]({static}/images/My_GPSMAP_66sr_Config/596.png)

Side notes, contrary to the 66sr user manual, [the 66sr does not have WAAS/EGNOS](https://support.garmin.com/en-US/?faq=QciNGsFuPs1CeNvI9OAhI6). "This is due to the multi-band technology" according to the Garmin support team. Also, notice that the 66sr turns off below -20 degC, whereas the 64sc is working fine below -26. That is an issue for my winter trips. One would recommend to keep the battery on the warm body, but the 66sr battery cannot be removed.

## TopoActice: Off

TopoActive maps are not needed, they do not include DEM data, and POIs are anyway included in Garmin TOPO PRO maps and 3rd party OSM-based maps. The internal storage could therefore be used for actually useful maps.

## Map of Finland, Sweden, Norway

A free and good topo map of Finland is MTK Suomi ([website](https://kartat.hylly.org/), [GitHub](https://github.com/pailakka/mtk2garmin)). It really looks like the government map. On my trip to Sweden, I used the [Frikart.no](http://www.frikart.no/garmin/velgkart.html) maps. They are not okay for off-track navigation but at least it is loading fine and good enough alongside the paper map. The expensive TOPO Sweden v6 map by Garmin is not working with the 66sr and not displayed properly on the 64sc (I sent the map back and got refund). The TOPO Norway PRO by Garmin is looking better than Frikart or [OpenTopoMap](https://garmin.opentopomap.org/) and loading okay. I did not try the Finnish map from Garmin since MTK Suomi is great.

## Garmin Topo Norway PRO

Notice that the official Garmin map of Norway (Topo Norway PRO) has two different line profiles, elevation line every 20m or elevation line every 10m. The change is sudden and may be confusing at first:

![Maps]({static}/images/My_GPSMAP_66sr_Config/325.png)

## DEM

Free maps do not include Digital Elevation Model (DEM), but it can be downloaded from [alternativaslibres.org](https://alternativaslibres.org/en/dem.php) generated with data provided by AW3D30 of the Japan Aerospace Exploration Agency, created with mkgmap and splitter. Notice that DEM data will still be available even if the DEM map is disabled, so MTK Suomi is enabled for viewing the map and DEM is disabled but used for elevation data.

![Maps]({static}/images/My_GPSMAP_66sr_Config/613.png)

Information without DEM:

![Information without DEM]({static}/images/My_GPSMAP_66sr_Config/103.png)

Information with DEM:

![Information with DEM]({static}/images/My_GPSMAP_66sr_Config/171.png) ![Elevation profile]({static}/images/My_GPSMAP_66sr_Config/201.png)

## Startup Message

The startup message can be edited. I added my name and contact information in case I lose my device.

## Storages

The planned tracks/routes (GPX files) have to be in the external SD card (into /Garmin/GPX/) to be used for navigation. On the other hand, uploading the route from the Garmin Explore mobile app into the internal storage is okay. The 64sc can have the GPX in the internal memory (in /Garmin/GPX/).

Maps can be either in the internal or the external storage.

## Logging

### GPX Data

Save points with interval in distance so that the track is clean. On the other hand, if saving every minute, there might be some noise during snack breaks.

![Tracking Options]({static}/images/My_GPSMAP_66sr_Config/1076.png)

### RINEX: Off

[RINEX is a new feature](https://support.garmin.com/en-US/?faq=7iMJZdoCcM2562XlKlMC76) I do not need. It takes lots of internal memory, and probably consuming battery to save the files. Therefore, it is disabled.

![RINEX Logging Off]({static}/images/My_GPSMAP_66sr_Config/55.png)

## Other Stuff

### Position Format For Sweden

Always carry a paper map. In Sweden, the position format is SWEREF 99 TM. To ease locating yourself on the paper map, the device can have the same position format.

![Position format]({static}/images/My_GPSMAP_66sr_Config/1422.png)

### Compass & Map Settings

I always re-calibrate my compass at the beginning of every trip. Despite calibration, the compass is not so accurate and I like the map to be still, so my North Reference is Grid.

![North reference]({static}/images/My_GPSMAP_66sr_Config/1795.png)

If using vector maps, the amount of details can be changed:

![Amount of details]({static}/images/My_GPSMAP_66sr_Config/698.png)

### Routing & Course Alerts

I go off-track, so routing is direct and unlocked. Also, I was happily surprised to see a new option after the firmware update: it is possible to disable course alerts to avoid the annoying "bip" when the planned track is well detailed but not following your actual path.

![Course alerts]({static}/images/My_GPSMAP_66sr_Config/109.png)

### Power Saving

![Power saving options]({static}/images/My_GPSMAP_66sr_Config/630.png)

The backlight is off. Overnight, I prefer to use my headlight to see the screen. The GPS 66sr battery cannot be removed whereas my light is easy to charge and I have extra batteries.
