import Gaffer

# The limit is specified in bytes, the following sets an 4GB cache
print ("LDTGAFFER:startup:Gaffer:cacheMemoryLimit: Setting memory limit to 4GB")
Gaffer.ValuePlug.setCacheMemoryLimit( 4 * 1024 * 1024 * 1024 )
