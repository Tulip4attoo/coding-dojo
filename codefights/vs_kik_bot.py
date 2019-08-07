def spamDetection(messages, spamSignals):
    result = []
    result.append(lack_of_content_rule(messages))
    result.append(duplicated_content_to_receiver_rule(messages))
    result.append(duplicated_content_from_sender_rule(messages))
    result.append(spam_signals_rule(messages, spamSignals))
    return result

def reduce_fraction(numerator, denominator):
    max_divisor = get_max_divisor(numerator, denominator)
    numerator, denominator = numerator / max_divisor, denominator / max_divisor
    return numerator, denominator

def get_max_divisor(x, y):
    while x > 0:
        tmp = x
        x = y % x
        y = tmp
    return tmp

def lack_of_content_rule(messages):
    '''
    as known as rule 1
    more than 90 % of all messages had fewer than 5 words (here, a word is 
    defined as a sequence of consecutive Latin letters which is neither preceded
    nor followed by a Latin letter);
    '''
    number_of_messages = len(messages)
    count_short_message = 0
    for message in messages:
        if len(message[0].split(' ')) < 5:
            count_short_message += 1
    if count_short_message * 100 <= 90 * number_of_messages:
        return 'passed'
    else:
        numerator, denominator = reduce_fraction(count_short_message, \
            number_of_messages)
        return 'failed: {0}/{1}'.format(numerator, denominator)

def duplicated_content_to_receiver_rule(messages):
    '''
    as known as rule 2
    more than 50 % of messages to any one user had the same content, assuming 
    that there were at least 2 messages to that user;
    '''
    check_list = []
    duplicated_message_dict = {}
    count_receiver_id_dict = {}
    count_message_per_id_dict = {}
    for message in messages:
        receiver_id = message[1]
        text = message[0]
        if receiver_id not in count_message_per_id_dict:
            count_message_per_id_dict[receiver_id] = 1
        else:
            count_message_per_id_dict[receiver_id] += 1
        if message not in check_list:
            check_list.append(message)
            duplicated_message_dict[receiver_id] = {}
        else:
            if text not in duplicated_message_dict[receiver_id]:
                duplicated_message_dict[receiver_id][text] = 2
            else:
                duplicated_message_dict[receiver_id][text] += 1
    result_list = get_list_half_spam(duplicated_message_dict, \
                                                count_message_per_id_dict)
    if len(result_list) == 0:
        return 'passed'
    else:
        result_list.sort()
        return 'failed: ' + ' '.join(result_list)

def get_list_half_spam(duplicated_message_dict, count_message_per_id_dict):
    result_list = []
    for receiver_id in duplicated_message_dict:
        number_of_messages = count_message_per_id_dict[receiver_id]
        for text in duplicated_message_dict[receiver_id]:
            if duplicated_message_dict[receiver_id][text] * 100 <= 50 * \
                                                            number_of_messages:
                continue
            else:
                result_list.append(receiver_id)
                break
    return result_list

def duplicated_content_from_sender_rule(messages):
    '''
    as known as rule 3
    more than 50 % of all messages had the same content, assuming that there 
    were at least 2 messages;
    '''
    if len(messages) < 2:
        return 'passed'
    else:
        check_list = []
        count_dict = {}
        for message in messages:
            text = message[0]
            if text in check_list:
                if text not in count_dict:
                    count_dict[text] = 2
                else:
                    count_dict[text] += 1
            else:
                check_list.append(text)

        number_of_messages = len(messages)
        max_duplicated_content, duplicated_content = \
            get_max_duplicated_content(count_dict)
        if max_duplicated_content * 100 <= 50 * number_of_messages:
            return 'passed'
        else:
            return 'failed: {}'.format(duplicated_content)

def get_max_duplicated_content(count_content_dict):
    max_duplicated_content = 0
    if len(count_content_dict) == 0:
        return 1, 'no_text'
    for text in count_content_dict:
        if max_duplicated_content < count_content_dict[text]:
            max_duplicated_content = count_content_dict[text]
            duplicated_content = text
    return max_duplicated_content, duplicated_content


def spam_signals_rule(messages, spamSignals):
    '''
    as known as rule 4
    more than 50 % of all messages contained at least one of the words from the 
    given list of spamSignals (the letters' case doesn't matter).
    '''
    number_of_messages = len(messages)
    spamSignals_list = []
    count_spamSignals_message = 0
    for message in messages:
        lower_text = message[0].lower()
        for ch in ['!','.', ',', '?']:
            if ch in lower_text:
                lower_text = lower_text.replace(ch, '')
        process_text_list = lower_text.split(' ')
        for spamSignal in spamSignals:
            if spamSignal in process_text_list:
                count_spamSignals_message += 1
                spamSignals_list.append(spamSignal)
    if count_spamSignals_message * 100 <= 50 * number_of_messages:
        return 'passed'
    else:
        spamSignals_list = list(set(spamSignals_list))
        spamSignals_list.sort()
        return 'failed: {}'.format(' '.join(spamSignals_list))