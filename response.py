def response(temp, model, f_temp, c_temp, nfpa_72_requirement, head, material):  
  requirement = '' if nfpa_72_requirement == 's' else 'no '
  thread = 'rosca simple' if head == 'hexagonal' else 'rosca doble'  

  return f"""
    Dado que la temperatura máxima al interior del recinto es de {f_temp} °F ({c_temp} °C), la temperatura mínima de seteo es de {f_temp + 100} °F ({round(5*(f_temp+100-32)/9, 2)} °C).
    Lo anterior se deba a que la temeratura de seteo debe ser por lo menos 100 °F mayor a la temperatura máxima esperada. 
    Además de lo anterior, {requirement}se requiere que el detector cumpla con los requerimientos de de la NFPA 72 para ser un dispositivo
    de activación, que la cabeza del dipositivo sea de tipo {head} ({thread}) y que su cabeza sea de {material}.

    Los detectores D.A.F no son sensibles a la posición. La denominación detector vertical u horizontal se refiere la la configuración más común de montaje de los detectores, es decir,
    cada detector puede montarse tanto vertical como horizontalmente en función de los requerimientos de la aplicación. 

    Dato todo lo dicho anteriormente ha seleccionado un detector con modelo {model['model_number'].values[0]} con las siguientes características:

    *Modelo: {model['model_number'].values[0]}
    *Material de la cabeza: {material}
    *Tipo de cabeza: {head} ({thread})
    *Tipo de contacto: {model['contact_operation'].values[0]}
    *Rating eléctrico: {model['electrical_rating_resistive_only'].values[0]}
    *Temperatura de seteo: {temp['f_setting'].values[0]} °F ({temp['c_setting'].values[0]} °C) 
    *Tolerancia: {temp['f_tolerance'].values[0]} °F ({temp['c_tolerance'].values[0]} °C) 
    *Espaciamiento UL: {temp['spacing_UL_feet'].values[0]} ft
    *Espaciamiento ULC: {temp['spacing_ULC_feet'].values[0]} ft
    *Espaciamiento FM: {temp['spacing_FM_feet'].values[0]}  ft
    *Espaciamiento RTI clasificado: {model['rti_rated_spacing'].values[0]}. Los espacios mostrados son distancias entre detectores en techos lisos, las distancias desde particiones o paredes serían la mitad de las mostradas. Se debe consultar a la autoridad competente (AHJ) antes de la instalación.
    *RTI: {temp['rti_response'].values[0]} (ft*s)^0.5
    *Clasificación RTI: ({temp['rti'].values[0]})
    *Código de color: {temp['color_coding'].values[0]}     
    *Clasificación de áreas: {model['hazardouz_location'].values[0]}
    *Montaje: {model['mounting_fitting'].values[0]}
    *Pedido: {model['model_number'].values[0]} at {temp['f_setting'].values[0]} °F
  """
