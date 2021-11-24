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
	interactive_plugs = {
					"driverType" : "ClientDisplayDriver",
					"displayHost" : "localhost",
					"displayPort" : "${image:catalogue:port}",
					"remoteDisplayType" : "GafferImage::GafferDisplayDriver",
					"filter" : "box"
				}
	batch_plugs = {
				}
	
	lightgroup_list = [
						'lightgroup_a',
						'lightgroup_b',
						'lightgroup_c',
						'lightgroup_d',
						'lightgroup_e',
						'lightgroup_f',
						'lightgroup_g',
						'lightgroup_h',
						'lightgroup_i',
						'lightgroup_j',
						'lightgroup_k']
						#'lightgroup_l',
						#'lightgroup_m',
						#'lightgroup_n',
						#'lightgroup_o',
						#'lightgroup_p',
						#'lightgroup_q',
						#'lightgroup_r'
						#'lightgroup_s',
						#'lightgroup_t',
						#'lightgroup_v',
						#'lightgroup_w',
						#'lightgroup_x',
						#'lightgroup_y',
						#'lightgroup_z']"""
	
	lightgroup_components = {
		"specular_direct":"lpe C<RS><L.'lightgroup'>",
		"specular_indirect":"lpe C<RS>[DSVOB].*<L.'lightgroup'>",
		"diffuse_direct":"lpe C<RD><L.'lightgroup'>",
		"diffuse_indirect":"lpe C<RD>[DSVOB].*<L.'lightgroup'>",
		"sss":"lpe C<TD>.*<L.'lightgroup'>",
		"volume":"lpe CV.*<L.'lightgroup'>"
	}

	for lightgroup in lightgroup_list:
		label = lightgroup.replace( "_", " " ).title().replace( " ", "_" )

		lightgroup_letter = lightgroup.split("_")[1]

		# Main Lightgroups OUTPUT
		GafferScene.Outputs.registerOutput(
			"Interactive/Arnold/" + label,
			IECoreScene.Output(
				lightgroup,
				"ieDisplay",
				"lpe " + "C.*[<L.'%s'>V]" %(lightgroup_letter),
				interactive_plugs
			)
		)
		GafferScene.Outputs.registerOutput(
			"Batch/Arnold/" + label,
			IECoreScene.Output(
				"${project:rootDirectory}/renders/${script:name}/%s/%s.####.exr" % ( lightgroup, lightgroup ),
				"exr",
				"lpe " + "C.*[<L.'%s'>V]" %(lightgroup_letter),
				batch_plugs
			)
		)
		# Lightgroups Components Outputs
		for component in lightgroup_components.keys():
			component_label = label + "_" + component
			component_name = lightgroup + "_" + component
			data = lightgroup_components[component].replace("lightgroup", lightgroup_letter)
			GafferScene.Outputs.registerOutput(
				"Interactive/Arnold/" + component_label,
				IECoreScene.Output(
					component_name,
					"ieDisplay",
					data,
					interactive_plugs
				)
			)
			GafferScene.Outputs.registerOutput(
				"Batch/Arnold/" + component_label,
				IECoreScene.Output(
					"${project:rootDirectory}/renders/${script:name}/%s/%s.####.exr" % ( component_name, component_name ),
					"exr",
					data,
					batch_plugs
				)
			)

	# Other custom outputs
	custom_outputs = {
		"denoise_albedo":"denoise_albedo",
		"emission_indirect":"lpe C.O",
		"Pref":"Pref vector",
		"raycount":"raycount float",
		"nlights":"color nlights",
		"cputime":"cputime float"
	}

	for output in custom_outputs.keys():
		label = output.replace( "_", " " ).title().replace( " ", "_" )

		GafferScene.Outputs.registerOutput(
			"Interactive/Arnold/" + label,
			IECoreScene.Output(
				output,
				"ieDisplay",
				custom_outputs[output],
				interactive_plugs
			)
		)
		GafferScene.Outputs.registerOutput(
			"Batch/Arnold/" + label,
			IECoreScene.Output(
				"${project:rootDirectory}/renders/${script:name}/%s/%s.####.exr" % ( output, output ),
				"exr",
				custom_outputs[output],
				batch_plugs
			)
		)
