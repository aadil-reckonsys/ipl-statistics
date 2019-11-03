from celery import shared_task
from matches.models import Match, Delivery
import logging
logger = logging.getLogger(__file__)


@shared_task
def upload_matches(matches):
    from matches.service.match_service import MatchService
    match_list = []
    logger.info('Match uploading started')
    for match in matches:
        if not Match.objects.filter(id=match['id']).exists():
            match_list.append(Match(**match))
    Match.objects.bulk_create(match_list)
    logger.info('Match uploading done')
    MatchService().clear_cache()


@shared_task
def upload_deliveries(deliveries):
    from matches.service.match_service import MatchService
    delivery_list = []
    logger.info('Delivery uploading started')
    for delivery in deliveries:
        delivery['match'] = Match.objects.get(id=delivery['match_id'])
        del delivery['match_id']
        if not Delivery.objects.filter(**delivery).exists():
            delivery_list.append(Delivery(**delivery))
    Delivery.objects.bulk_create(delivery_list)
    logger.info('Delivery uploading done')
    MatchService().clear_cache()
