# REPLACE THE OSLC PATH WITH YOUR OWN
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR/osl
#find $SCRIPT_DIR/osl -type f -printf ":%p"
find $SCRIPT_DIR -type f -iname '*.osl' -exec /opt/gaffer/bin/oslc -Ipath $SCRIPT_DIR/osl/include {} \; > results.out
cd -