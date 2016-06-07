import extract_event as ee
import event_functions as ef
import body

document = {}
document['head'] = 'Showing of Orca'
document['body'] = body.body

venues = ef.load_venues('venues_updated.json')
event = ee.Extract_event(document)
event.pos_tag()
event.extract_venue(venues)
event.extract_time()
event.info()
