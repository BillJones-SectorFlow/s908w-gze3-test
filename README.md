# SM-S908W GZE3 experimental phone test

The repository is prepared for Root My Galaxy Next. No catalog preparation or computer upload is required.

**Experimental: compiled and checked on the build machine, but never tested on a phone.** Kernel exploit attempts can crash or reboot the phone. Back up important files before testing.

Use only this exact device and firmware:

| Item | Required value |
|---|---|
| Model | `SM-S908W` |
| Firmware | `S908WVLSAGZE3` |
| Full kernel release | `5.10.236-android12-9-31998796-abS908WVLSAGZE3` |
| Payload source repository | `BillJones-SectorFlow/s908w-gze3-test` |
| Branch | `main` |
| Target | `Galaxy S22 Ultra SM-S908W \| GZE3 \| EXPERIMENTAL v1` |
| Flavor | `KernelSU-Next` |

## Downloads and installation order

1. Install the [matching KernelSU-Next v3.4.0 manager APK](https://raw.githubusercontent.com/BillJones-SectorFlow/s908w-gze3-test/main/manager/KernelSU_Next_v3.4.0-android12-5.10_33303-release.apk) using Android's installer. This is the unchanged sarabpal-dev APK; its signer matches the embedded module. Installing it alone does not root the phone. If Android reports a signature/package conflict, resolve that before continuing.
2. Install [Root My Galaxy Next v0.10](https://github.com/rushiranpise/Root-My-Galaxy-Next/releases/download/v0.10/RootMyGalaxyNext-0.10.apk). Use this release for the first test: its tag resolves to the revision recorded in [PROVENANCE.json](PROVENANCE.json). The original Root My Galaxy app is a different app.
3. Save the [experimental `.so` payload](https://raw.githubusercontent.com/BillJones-SectorFlow/s908w-gze3-test/main/artifacts/ionstack-s908w-gze3-rmgnext-experimental.so) to the phone for the Local payload picker below.

Next v0.10 checks for an installed manager of the chosen flavor before downloading one. Keep the matching manager above installed. Confirm Next's Home status recognizes KernelSU-Next, and do not use Next's manager download/update action to replace it: the offered stock manager has a different signer. No modified Next APK is needed for this setup.

## Configure Next

1. Start Shizuku through its normal wireless-debugging setup, then authorize Next. In **Settings → Shizuku Management**, enable **Use Shizuku**. This payload requires shell UID 2000 and refuses a native app-process run.
2. Keep every automatic rooting-on-boot option, automatic retry, and automatic soft restart disabled for this first test.
3. Open **Settings → Payload Management → Payload Sources → Add**. Enter repository `BillJones-SectorFlow/s908w-gze3-test` and branch `main`. Enable this source. To keep the first test unambiguous, disable the other payload sources for now.
4. Check the source: it contains one payload and should report a match for your phone. If it reports no match, **stop**. Do not select another phone's target. Use the source's lock action to pin the current uploaded commit, then apply **Pin**.
5. Open **Settings → Payload Management → Local payload** and select `ionstack-s908w-gze3-rmgnext-experimental.so`.
6. Use the normal device payload flow and select **Galaxy S22 Ultra SM-S908W | GZE3 | EXPERIMENTAL v1** from **your repository**. Choose **KernelSU-Next** if asked. Avoid the universal/Dirty Frag flow.
7. Use **Online** mode for the first install, and leave **Install KernelSU** enabled. Online mode fetches the custom loader from this repository and checks its catalog hash. Local import replaces only the exploit, so the hosted source is still required. Leave run limits at their defaults.

## Run one test

Keep the screen on and run the normal install/root action once. Do not start another run concurrently. The experimental payload caps itself at one attempt and discards cached slide offsets.

If the run fails or times out, export **History / Run details** and reboot before another attempt. If Next reports success, open the preinstalled matching KernelSU-Next manager and check that it reports a working driver/root. Next's success message alone does not verify the manager end to end. Save the run log either way.

Avoid soft restarts, root modules, and root-on-boot setup during this first test.

## Limits and recovery

Root is expected to last until a full reboot; this kit does not flash the boot image. The loader writes its daemon/assets under `/data/adb`; ephemeral mode skips root-module lifecycle scripts. It refuses to overwrite a different existing `/data/adb/ksud`.

Local import persists until removed. Remove it before selecting any other target. Re-enable your usual sources after ending this test if needed.

## Files and evidence

- [support/targets-v3.json](support/targets-v3.json): schema-v3 catalog with the exact model/kernel, configured download URLs, sizes, and SHA-256 hashes.
- [artifacts/](artifacts/): experimental exploit and custom loader.
- [manager/](manager/): unchanged matching manager APK.
- [PROVENANCE.json](PROVENANCE.json): upstream revisions, reported build checks, and limitations.
- [source/](source/): modified source archives, patches, upstream licenses, and build notes.
- [START-HERE.txt](START-HERE.txt): original detailed procedure, updated with this account and prepared-repository notice.
- [SHA256SUMS](SHA256SUMS): checksums of published files; verify on a computer with `sha256sum -c SHA256SUMS`.

The setup instructions are based on the packaged START-HERE procedure and the inspected [Next v0.10 source](https://github.com/rushiranpise/Root-My-Galaxy-Next/tree/bca6761062a7142b30fb80a081669b9975e9dde3). Repository checks establish file integrity and hosted availability; they do not establish runtime exploit or module compatibility on the phone. Changes to the payloads, firmware, or Next version require fresh verification.
