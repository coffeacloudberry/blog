Title: Setup QMapShack For Norway
Date: 2024-02-22 00:00
Category: Outdoor Tips
Summary: Configure the map and coordinates to match the Norge-serien topo maps with QMapShack

# Map Layer

Use the *Norway Topo* maps from the Norwegian Mapping Authority (Statens kartverk). The layer is almost identical to the [Kartverket](https://www.norgeskart.no/#!?project=norgeskart&layers=1002&zoom=12&lat=7861962.42&lon=949126.47) map and the [Norge-serien paper maps](https://www.dntbutikken.no/kart).

# Map Grid

![QMapShack grid overview]({static}/images/QMapShack_For_Norway/qmapshack_norway.png){: .image-process-article-image}

The Norge-serien paper topo maps are using the [EUREF89](https://en.wikipedia.org/wiki/European_Terrestrial_Reference_System_1989) datum. The grid is projected with the [Universal Transverse Mercator (UTM)](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system). The grid zone is written on the map, panning from [zone 32 to 36](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system#/media/File:Modified_UTM_Zones.png). To change the grid, go to View -> Setup Grid and type `+proj=utm +zone=35 +units=m +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs +type=crs` (change the zone to yours). The QMapShack documentation related to the [CRS](https://pygis.io/docs/d_crs_what_is_it.html) is [here](https://github.com/Maproom/qmapshack/wiki/EpsgOverview#properties-of-some-commonly-used-coordinate-systems).

![UTM zones]({static}/images/QMapShack_For_Norway/modified_UTM_zones.png){: .image-process-article-image}

# GPS Format

The GPS location can be changed to match the paper map that uses N??°?? E??°??. Go to View -> Setup Coord. Format.
