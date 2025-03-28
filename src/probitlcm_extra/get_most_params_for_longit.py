# This file is part of "probitlcm_extra" which is released under GPL v3.
#
# Copyright (c) 2022-2025 Eric Alan Wayman <ericwaymanpublications@mailworks.org>.
#
# This program is FLO (free/libre/open) software: you can redistribute
# it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse, json, pathlib, shutil

def get_most_params_for_longit(run_dir, cross_sec_dir_name, longit_dir_name,
                               total_num_of_scenarios):
    cross_sec_scenario_files_path = run_dir.joinpath(cross_sec_dir_name,
                                                     "scenario_files")
    longit_scenario_files_path = run_dir.joinpath(longit_dir_name,
                                                  "scenario_files")
    for scenario_number in range(1, total_num_of_scenarios + 1):
        scenario_number_padded = f"{scenario_number:04}"
        scenario_dir_name = "scenario_" + scenario_number_padded
        src_path = cross_sec_scenario_files_path.joinpath(
            scenario_dir_name, "datagen_params")
        dest_path = longit_scenario_files_path.joinpath(
            scenario_dir_name, "datagen_params")
        shutil.copytree(src_path, dest_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--cross_sec_dir_name', required=True)
    parser.add_argument('--longit_dir_name', required=True)
    parser.add_argument('--total_num_of_scenarios', required=True)
    # parse arguments
    args = parser.parse_args()
    run_dir = pathlib.Path.cwd()
    cross_sec_dir_name = args.cross_sec_dir_name
    longit_dir_name = args.longit_dir_name
    total_num_of_scenarios = int(args.total_num_of_scenarios)
    # get scenarios list
    run_dir = pathlib.Path.cwd()
    get_most_params_for_longit(run_dir, cross_sec_dir_name, longit_dir_name,
                               total_num_of_scenarios)


