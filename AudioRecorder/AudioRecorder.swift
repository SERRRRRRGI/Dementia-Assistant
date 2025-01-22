import AVFoundation

class AudioRecorder {
    static let shared = AudioRecorder() // Singleton instance
    private var audioRecorder: AVAudioRecorder?

    private init() {}

    /// Requests microphone permission using the older, widely compatible API.
    func requestMicrophonePermission(completion: @escaping (Bool) -> Void) {
        let audioSession = AVAudioSession.sharedInstance()
        // Use the old API for requesting microphone permission
        audioSession.requestRecordPermission { granted in
            DispatchQueue.main.async {
                completion(granted)
            }
        }
    }

    /// Starts audio recording.
    func startRecording() {
        let audioSession = AVAudioSession.sharedInstance()
        do {
            // Configure the audio session for recording
            try audioSession.setCategory(.playAndRecord, mode: .default, options: [.defaultToSpeaker])
            try audioSession.setActive(true)

            // Define the file URL for saving the recording
            let fileURL = getDocumentsDirectory().appendingPathComponent("recording.m4a")
            let settings: [String: Any] = [
                AVFormatIDKey: Int(kAudioFormatMPEG4AAC),
                AVSampleRateKey: 44100,
                AVNumberOfChannelsKey: 2,
                AVEncoderAudioQualityKey: AVAudioQuality.high.rawValue
            ]
            
            // Initialize the audio recorder and start recording
            audioRecorder = try AVAudioRecorder(url: fileURL, settings: settings)
            audioRecorder?.record()

            print("Recording started! File saved at: \(fileURL.path)")
        } catch {
            print("Failed to start recording: \(error)")
        }
    }

    /// Stops audio recording.
    func stopRecording() {
        audioRecorder?.stop()
        print("Recording stopped.")
    }

    /// Returns the directory for saving audio recordings.
    private func getDocumentsDirectory() -> URL {
        return FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
    }
}
