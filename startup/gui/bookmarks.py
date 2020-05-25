import os

import GafferUI

print ("LDTGAFFER:startup:gui:bookmarks")

bookmarks = GafferUI.Bookmarks.acquire( application )
bookmarks.add( "LDTGAFFER", os.path.expandvars( "$LDTGAFFER" ) )
bookmarks.add( "LDTGAFFER_EXTENSIONS", os.path.expandvars( "$GAFFER_EXTENSION_PATHS" ) )
bookmarks.add( "LDTGAFFER_REFERENCE", os.path.expandvars( "$GAFFER_REFERENCE_PATHS" ) )
bookmarks.add( "GAFFER_EXAMPLES", os.path.expandvars( "$GAFFER_EXAMPLES" ) )

bookmarks.setDefault( os.path.expandvars( "$LDTGAFFER" ) )