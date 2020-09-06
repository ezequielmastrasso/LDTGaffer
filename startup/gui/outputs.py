import GafferScene
import IECore
import IECoreScene


print ("LDTGAFFER:startup:gui:outputs")

# Re-register outputs to change the default fileName plug
# ${output_fileName} is set on the customVariables

with IECore.IgnoredExceptions( ImportError ) :

	# If Arnold isn't available for any reason, this will fail
	# and we won't add any unnecessary output definitions.
	import GafferArnold
	
	for lightgroup in [
		'lightgroup_a',
		'lightgroup_a_denoise',
		'lightgroup_b',
		'lightgroup_b_denoise',
		'lightgroup_c',
		'lightgroup_c_denoise',
		'lightgroup_d',
		'lightgroup_d_denoise',
		'lightgroup_e',
		'lightgroup_e_denoise',
		'lightgroup_f',
		'lightgroup_f_denoise',
		'lightgroup_g',
		'lightgroup_g_denoise',
		'lightgroup_h',
		'lightgroup_h_denoise',
		'lightgroup_i',
		'lightgroup_i_denoise'
	]:
		label = lightgroup.replace( "_", " " ).title().replace( " ", "_" )

		lightgroup_letter = lightgroup.replace("_denoise","").split("_")[1]
		data="C.*[<L.'%s'>V]" %(lightgroup_letter)

		interactive_plugs = {
					"driverType" : "ClientDisplayDriver",
					"displayHost" : "localhost",
					"displayPort" : "${image:catalogue:port}",
					"remoteDisplayType" : "GafferImage::GafferDisplayDriver",
					"filter" : "box"
				}
		batch_plugs = {
		}

		if "denoise" in lightgroup:
			interactive_plugs['filter'] = 'denoise_optix'
			batch_plugs['filter'] = 'denoise_optix'

		GafferScene.Outputs.registerOutput(
			"Interactive/Arnold/" + label,
			IECoreScene.Output(
				lightgroup,
				"ieDisplay",
				"lpe " + data,
				interactive_plugs
			)
		)

		GafferScene.Outputs.registerOutput(
			"Batch/Arnold/" + label,
			IECoreScene.Output(
				"${project:rootDirectory}/renders/${script:name}/%s/%s.####.exr" % ( lightgroup, lightgroup ),
				"exr",
				"lpe " + data,
				batch_plugs
			)
		)

