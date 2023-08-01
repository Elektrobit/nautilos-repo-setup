#!/bin/bash
# NautilOS profile environment

set -e

A_DOMAIN=linux.elektrobit.com
A_PRODUCT=corbos


function clean_repo {
    rm -f /etc/apt/sources.list.d/${A_PRODUCT}*.sources
}

function init_auth {
    echo 'APT { Get { AllowUnauthenticated "1"; }; };' \
        > /etc/apt/apt.conf.d/99allow_unauth
}

function add_repo_key {
    local A_VERSION=$1
    local A_PHASE=$2
    local A_REPO=$3
    local key_name
    key_name=$(echo "${A_PRODUCT}-${A_VERSION}-${A_PHASE}-${A_VERSION}-${A_PHASE}-${A_REPO}.asc" | tr '/' '_')
    sudo curl -L \
        "https://$A_DOMAIN/$A_PRODUCT/$A_VERSION/$A_PHASE/$A_REPO/Release.key" \
        | cat > /etc/apt/trusted.gpg.d/"${key_name}"
}

function add_repo {
    local A_VERSION=$1
    local A_PHASE=$2
    local A_REPO=$3
    local source_file_name
    add_repo_key "$A_VERSION" "$A_PHASE" "$A_REPO"
    source_file_name=$(echo "${A_PRODUCT}-${A_VERSION}-${A_PHASE}-${A_REPO}") 
    cat >/etc/apt/sources.list.d/"${source_file_name}".sources <<- EOF
		Types: deb
		URIs: https://$A_DOMAIN/$A_PRODUCT/$A_VERSION/$A_PHASE/$A_REPO
		Suites: ./
		trusted: yes
		check-valid-until: no
	EOF
}

function get_repo_server {
    echo "https://$A_DOMAIN/$A_PRODUCT/"
}


ARGUMENT_LIST=(
    "version:"
    "phase:"
)

# read arguments
if ! opts=$(getopt \
    --longoptions "$(printf "%s," "${ARGUMENT_LIST[@]}")" \
    --name "$(basename "$0")" \
    --options "" \
    -- "$@"
); then
    echo "bootstrap.sh"
    echo "  --version <number>"
    echo "      version number"
    echo "  --phase <tags>"
    echo "      such as sp1 (service pack 1)"
    exit 1
fi

eval set --"${opts}"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --version)
            version=$2
            shift 2
            ;;

        --phase)
            phase=$2
            shift 2
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "Invalid option: $1"
            exit 1
            ;;
    esac
done


echo "Setup ${A_PRODUCT} repositories..."
clean_repo

# corbos public repositories
echo ${dist_mode}
add_repo "${version}" "${phase}" containers
add_repo "${version}" "${phase}" xUbuntu_22.04_debbuild

apt-get update
