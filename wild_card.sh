#!/bin/bash

#THIS CHECKS IF THE DOMAIN HAS A WILDCARD CONFIG
#TESTS RANDOM SUBDOMAINS THAT SHOULDNT RETURN

#argv1 = domain

if [ $# -ne 1 ]; then
	echo "wrong";
	exit 1;
fi

wildcardactive=$(dig @1.1.1.1 A,CNAME {test321123,testingforwildcard,plsdontgimmearesult}.$1 +short | wc -l)

[ $wildcardactive ] && echo "wildcare config is active"
[ ! $wildcardactive ] && echo "wildcare config is not active"


